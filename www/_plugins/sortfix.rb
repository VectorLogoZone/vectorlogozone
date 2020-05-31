# frozen_string_literal: true

module Jekyll
  module Drops
    class PageDrop < Drop
      def sort
        @obj.data["sort"]
      end
    end
  end
end
